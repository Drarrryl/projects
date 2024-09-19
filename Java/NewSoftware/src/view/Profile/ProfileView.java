package view.Profile;

import entity.User;
import interface_adapter.Profile.ProfileController;
import interface_adapter.Profile.ProfileState;
import interface_adapter.Profile.ProfileViewModel;
import view.Game.BufferedImageLoader;
import view.View;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;

public class ProfileView extends View {

    private ProfileController controller;

    private JButton backButton;

    private SignupView signupView;

    public ProfileView(ProfileViewModel viewModel, ProfileController controller) {
        super(viewModel);
        this.controller = controller;

        JPanel footer = new JPanel();
        backButton = new JButton(viewModel.BACK_BUTTON_STRING);
        footer.add(backButton);
        footer.setLayout(new BoxLayout(footer, BoxLayout.X_AXIS));

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                controller.back();
            }
        });

        ProfilePanel profilePanel = new ProfilePanel(viewModel.getProfileState().getLoggedInUser(), viewModel);
        this.add(profilePanel);
        this.add(footer);
        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));

        viewModel.SetTheme(this, viewModel.getViewManager().getTheme());
    }

    private static class ProfilePanel extends JPanel implements Runnable {
        private User currUser;

        private JLabel username;
        private JLabel stats;
        private Canvas imageCanvas;
        private BufferedImage pfp;
        private boolean running;
        private Thread thread;

        private ProfileState state;
        private ProfileViewModel viewModel;
        public ProfilePanel(User user, ProfileViewModel viewModel) {
            this.currUser = user;
            this.viewModel = viewModel;

            state = viewModel.getProfileState();

            JPanel namePanel = new JPanel();
            username = new JLabel("[Insert Username]");
            namePanel.add(username);

            JPanel statsPanel = new JPanel();
            stats = new JLabel("[Insert Highscore]");
            statsPanel.add(stats);

            JPanel ImagePanel = new JPanel();
            JPanel NonImagePanel = new JPanel();

            BufferedImageLoader loader = new BufferedImageLoader();

            try {
                pfp = loader.loadImage("/images/pfp.png");
            } catch (Exception e) {
                e.printStackTrace();
            }

            imageCanvas = new Canvas();
            imageCanvas.setPreferredSize(new Dimension(50, 50));
            imageCanvas.setMinimumSize(new Dimension(50, 50));
            imageCanvas.setMaximumSize(new Dimension(50, 50));

            ImagePanel.add(imageCanvas);

            NonImagePanel.add(namePanel);
            NonImagePanel.add(statsPanel);
            NonImagePanel.setLayout(new BoxLayout(NonImagePanel, BoxLayout.Y_AXIS));

            state.addPropertyChangeListener(new PropertyChangeListener() {
                @Override
                public void propertyChange(PropertyChangeEvent evt) {
                    if (evt.getPropertyName().equals("status")) {
                        if (evt.getNewValue().equals(true)) {
                            updateInfo();
                            start();
                        }
                    }
                }
            });

            state.addPropertyChangeListener(new PropertyChangeListener() {
                @Override
                public void propertyChange(PropertyChangeEvent evt) {
                    if (evt.getPropertyName().equals("status")) {
                        if (evt.getNewValue().equals(false)) {
                            stop();
                        }
                    }
                }
            });

            this.add(ImagePanel);
            this.add(NonImagePanel);
            //this.setLayout(new BoxLayout(this, BoxLayout.X_AXIS));

            viewModel.SetTheme(this, viewModel.getViewManager().getTheme());
            viewModel.SetTheme(ImagePanel, viewModel.getViewManager().getTheme());
            viewModel.SetTheme(NonImagePanel, viewModel.getViewManager().getTheme());
        }

        private void updateInfo() {
            username.setText(state.getUsername());
            stats.setText("Highscore: " + state.getHighscore());
        }

        public synchronized void start() {
            if (running) {
                return;
            }

            running = true;

            thread = new Thread(this);
            thread.start();
        }

        public synchronized void stop() {
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

        public void tick() {

        }

        public void render() {
            BufferStrategy bs = imageCanvas.getBufferStrategy();

            if (bs == null) {
                imageCanvas.createBufferStrategy(3);
                return;
            }

            Graphics g = bs.getDrawGraphics();
            //////////////////////////////////

            g.drawImage(pfp, 0, 0, 50, 50, null);

            //////////////////////////////////
            g.dispose();
            bs.show();
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
            while (running) {
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
                    updates = 0;
                    frames = 0;
                }
            }
        }
    }
}
