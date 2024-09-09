package entity.Game;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public class TileObject extends GameObject implements Collidable {

    private double velX = -2.0;

    private final BufferedImage tile;
    private Obstacle obstacle;
    private ArrayList<BufferedImage> obstacles = new ArrayList<>();

    public boolean delete = false;
    public TileObject(double x, double y, HashMap<String, BufferedImage> tileSprites, boolean hasObstacle) {
        super(x, y, tileSprites.get("Grass").getWidth(), tileSprites.get("Grass").getHeight());

        tile = tileSprites.get("Grass");
        obstacles.add(tileSprites.get("Spikes"));

        if (hasObstacle) {
            obstacle = new Obstacle(x, y - obstacles.get(0).getHeight(), obstacles.get(0));
        } else {
            obstacle = null;
        }


    }

    public void setVelX(double velX) {
        this.velX = velX;
    }

    @Override
    public void tick(Canvas gameCanvas) {
        setX(getX() + velX);
        if (obstacle != null) obstacle.setX((getX() + velX));

        checkTilePos();
    }

    @Override
    public void render(Graphics g) {
        g.drawImage(tile, (int) getX(), (int) getY(), null);
        if (obstacle != null) {
            obstacle.render(g);
        }
    }

    public void checkTilePos() {
        if (getX() < -tile.getWidth()) {
            delete = true;
        }
    }
}
