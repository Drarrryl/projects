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

    private HashMap<String, BufferedImage> tileSprites;

    private Player plr;

    private JButton exitGameButton;

    private boolean running = false;
    private Thread thread;

    public GameView(GameViewModel viewModel, GameController gameController) {
        super(viewModel);
        this.gameController = gameController;

        float scale = 0.85f;
        final int WIDTH = (int) (viewModel.DEFAULT_SIZE.width * scale);
        final int HEIGHT = (int) (viewModel.DEFAULT_SIZE.height * scale);

        gameCanvas = new Canvas();
        gameCanvas.setPreferredSize(new Dimension(WIDTH, HEIGHT));
        gameCanvas.setMaximumSize(new Dimension(WIDTH, HEIGHT));
        gameCanvas.setMinimumSize(new Dimension(WIDTH, HEIGHT));
        gameCanvas.addKeyListener(new KeyInput(this));

        bgImage = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);

        BufferedImageLoader loader = new BufferedImageLoader();

        HashMap<String, BufferedImage> playerSprites = new HashMap<>();
        tileSprites = new HashMap<>();

        try {
            playerSprites.put("Idle", loader.loadImage("/images/idle.png"));
            playerSprites.put("Jump 1", loader.loadImage("/images/jump_1.png"));
            playerSprites.put("Jump 2", loader.loadImage("/images/jump_2.png"));

            tileSprites.put("Grass", loader.loadImage("/images/grass.png"));
            tileSprites.put("Spikes", loader.loadImage("/images/spikes.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        plr = new Player(200, 200, playerSprites);

        gameController.addObj(plr);

        viewModel.getViewManager().getApplicationFrame().setTitle(viewModel.TITLE);

        JPanel buttonPanel = new JPanel();
        exitGameButton = new JButton(viewModel.EXIT_GAME_BUTTON);
        buttonPanel.add(exitGameButton);

        exitGameButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                stop();
                viewModel.getState().setStatus(false);
            }
        });

        viewModel.getState().addPropertyChangeListener(
                new PropertyChangeListener() {
                    @Override
                    public void propertyChange(PropertyChangeEvent evt) {
                        if (evt.getPropertyName().equals("status")) {
                            if (evt.getNewValue().equals(true)) {
                                start();
                            }
                        }
                    }
        });

        this.add(gameCanvas);
        this.add(buttonPanel);
        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        viewModel.getViewManager().getApplicationFrame().pack();
        viewModel.SetTheme(this, viewModel.getViewManager().getTheme());
    }

    private synchronized void start() {
        if (running) {
            return;
        }

        running = true;

        gameCanvas.requestFocus();

        generateTiles(tileSprites);

        thread = new Thread(this);
        thread.start();
    }

    private synchronized void stop() {
        if (!running) {
            return;
        }

        running = false;
        try {
            thread.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

    }

    private void tick() {
        gameController.tick(gameCanvas);
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
        gameController.exitGame();
    }

    public void generateTiles(HashMap<String, BufferedImage> tiles) {
        int WIDTH = gameCanvas.getPreferredSize().width;
        int TILEWIDTH = tiles.get("Grass").getWidth();
        float ratio = (float) WIDTH / TILEWIDTH;
        int numTiles = Math.round(ratio);

        int HEIGHT = gameCanvas.getPreferredSize().height;
        int TILEHEIGHT = tiles.get("Grass").getHeight();
        double y = HEIGHT - TILEHEIGHT;

        for (int i = 0; i < numTiles; i++) {
            double x = (TILEWIDTH * i);
            gameController.addObj(new TileObject(x, y, tiles));
        }
    }
}
