package entity.Game;

import java.awt.*;
import java.awt.image.BufferedImage;

public class Obstacle extends GameObject implements Collidable {
    private BufferedImage obstacle;
    public Obstacle(double x, double y, BufferedImage obstacle) {
        super(x, y, obstacle.getWidth(), obstacle.getHeight());

        this.obstacle = obstacle;
    }

    @Override
    public void render(Graphics g) {
        g.drawImage(obstacle, (int) getX(), (int) getY(), null);
    }
}
