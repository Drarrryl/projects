package view.Game;

import entity.Game.Player;
import entity.Game.TileObject;
import interface_adapter.Game.GameController;
import interface_adapter.Game.GameViewModel;
import interface_adapter.Game.KeyInput;
import view.View;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.io.IOException;
import java.util.HashMap;

public class GameView extends View implements Runnable {

    private GameController gameController;

    private Canvas gameCanvas;

    private BufferedImage bgImage;

    HashMap<String, BufferedImage> playerSprites = new HashMap<>();
    private HashMap<String, BufferedImage> tileSprites;

    private Player plr;

    private long score;

    private JLabel scoreLabel;

    private JPanel buttonPanel;

    private JButton startButton;

    private JButton exitGameButton;

    private boolean running = false;
    private Thread thread;
    private String[] phase;

    public GameView(GameViewModel viewModel, GameController gameController) {
        super(viewModel);
        this.gameController = gameController;

        float scale = 0.8f;
        final int WIDTH = (int) (viewModel.DEFAULT_SIZE.width * scale);
        final int HEIGHT = (int) (viewModel.DEFAULT_SIZE.height * scale);

        gameCanvas = new Canvas();
        gameCanvas.setPreferredSize(new Dimension(WIDTH, HEIGHT));
        gameCanvas.setMaximumSize(new Dimension(WIDTH, HEIGHT));
        gameCanvas.setMinimumSize(new Dimension(WIDTH, HEIGHT));
        gameCanvas.addKeyListener(new KeyInput(this));

        BufferedImageLoader loader = new BufferedImageLoader();


        tileSprites = new HashMap<>();

        try {
            bgImage = loader.loadImage("/images/bg.png");

            playerSprites.put("Idle", loader.loadImage("/images/idle.png"));
            playerSprites.put("Jump 1", loader.loadImage("/images/jump_1.png"));
            playerSprites.put("Jump 2", loader.loadImage("/images/jump_2.png"));

            tileSprites.put("Grass", loader.loadImage("/images/grass.png"));
            tileSprites.put("Spikes", loader.loadImage("/images/spikes.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        plr = new Player(200, 200, playerSprites);

        score = 0;
        scoreLabel = new JLabel("Score: " + String.valueOf(score));

        viewModel.getViewManager().getApplicationFrame().setTitle(viewModel.TITLE);

        buttonPanel = new JPanel();
        startButton = new JButton(viewModel.START_GAME_BUTTON);
        exitGameButton = new JButton(viewModel.EXIT_GAME_BUTTON);
        buttonPanel.add(startButton);
        buttonPanel.add(exitGameButton);

        exitGameButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                stop();
                viewModel.getState().setStatus(false);
            }
        });

        startButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                start();
            }
        });

        viewModel.getState().addPropertyChangeListener(
                new PropertyChangeListener() {
                    @Override
                    public void propertyChange(PropertyChangeEvent evt) {
                        if (evt.getPropertyName().equals("status")) {
                            if (evt.getNewValue().equals(true)) {
                                init();
                            }
                        }
                    }
        });

        phase = new String[1];

        this.add(scoreLabel);
        this.add(gameCanvas);
        this.add(buttonPanel);
        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        viewModel.getViewManager().getApplicationFrame().pack();
        viewModel.SetTheme(this, viewModel.getViewManager().getTheme());
    }

    private void init() {
        if (running) {
            return;
        }

        running = true;

        phase[0] = "init";

        score = 0;
        if (((GameViewModel) getViewModel()).getLoggedInUser() != null) {
            scoreLabel.setText("Score: " + String.valueOf(score) + " Highscore: " + ((GameViewModel) getViewModel()).getLoggedInUser().getHighscore());
        }

        plr = new Player(200, 200, playerSprites);
        plr.setX(200);
        plr.setY(gameCanvas.getHeight()-plr.getHeight()-tileSprites.get("Grass").getHeight()+5);
        plr.setVelX(0);
        plr.setVelY(0);

        gameController.addObj(plr);

        generateTiles(tileSprites);

        thread = new Thread(this);
        thread.start();
    }

    private synchronized void start() {
        phase[0] = "start";

        score = 0;

        buttonPanel.remove(startButton);
        buttonPanel.updateUI();

        gameCanvas.requestFocus();
        gameCanvas.update(gameCanvas.getGraphics());
    }

    private synchronized void stop() {
        if (!running) {
            return;
        }

        phase[0] = "stop";

        buttonPanel.add(startButton, 0);

        running = false;
        gameController.resetObjs();

        try {
            thread.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

    }

    private void tick() {
        if (phase[0].equals("start")) {
            gameController.tick(gameCanvas, tileSprites, score);
            gameController.updatePlr(plr, phase);
            score += 1;
            scoreLabel.setText("Score: " + String.valueOf(score) + " Highscore: " + ((GameViewModel) getViewModel()).getLoggedInUser().getHighscore());
        }
    }

    private void render() {
        BufferStrategy bs = gameCanvas.getBufferStrategy();

        if (bs == null) {
            gameCanvas.createBufferStrategy(3);
            return;
        }

        Graphics g = bs.getDrawGraphics();
        //////////////////////////////////

        g.drawImage(bgImage, 0, 0, gameCanvas.getWidth(), gameCanvas.getHeight(), gameCanvas);

        gameController.render(g);

        //////////////////////////////////
        g.dispose();
        bs.show();
    }

    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();

        gameController.keyPressed(key, plr);
    }

    public void keyReleased(KeyEvent e) {
        int key = e.getKeyCode();

        gameController.keyReleased(key, plr);
    }

    @Override
    public void run() {
        long lastTime = System.nanoTime();
        final double amountOfTicks = 60.0;
        double ns = 1000000000 / amountOfTicks;
        double delta = 0;
        int updates = 0;
        int frames = 0;
        long timer = System.currentTimeMillis();
        while(running) {
            long now = System.nanoTime();
            delta += (now - lastTime) / ns;
            lastTime = now;
            if (delta >= 1) {
                tick();
                updates++;
                delta--;
            }
            render();
            frames++;

            if (System.currentTimeMillis() - timer > 1000) {
                timer += 1000;
                System.out.println(updates + " Ticks, Fps " + frames);
                updates = 0;
                frames = 0;
            }
        }
        gameController.exitGame(score, ((GameViewModel) getViewModel()).getLoggedInUser());
    }

    public void generateTiles(HashMap<String, BufferedImage> tiles) {
        int WIDTH = gameCanvas.getPreferredSize().width;
        int TILEWIDTH = tiles.get("Grass").getWidth();
        float ratio = (float) WIDTH / TILEWIDTH;
        int numTiles = Math.round(ratio) + 2;

        int HEIGHT = gameCanvas.getPreferredSize().height;
        int TILEHEIGHT = tiles.get("Grass").getHeight();
        double y = HEIGHT - TILEHEIGHT;

        for (int i = 0; i < numTiles; i++) {
            double x = (TILEWIDTH * i);
            gameController.addObj(new TileObject(x, y, tiles, false));
        }
    }

    public Canvas getGameCanvas() { return this.gameCanvas; }
}
