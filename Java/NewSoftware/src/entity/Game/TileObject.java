package entity.Game;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.ArrayList;
import java.util.HashMap;

public class TileObject extends GameObject implements Collidable {

    private double velX = -1.0;

    private final BufferedImage tile;
    private Obstacle obstacle;
    private ArrayList<BufferedImage> obstacles = new ArrayList<>();

    public boolean delete = false;
    public TileObject(double x, double y, HashMap<String, BufferedImage> tileSprites) {
        super(x, y, tileSprites.get("Grass").getWidth(), tileSprites.get("Grass").getHeight());

        tile = tileSprites.get("Grass");
        obstacle = null;
        obstacles.add(tileSprites.get("Spikes"));
    }

    public void setVelX(double velX) {
        this.velX = velX;
    }

    @Override
    public void tick(Canvas gameCanvas) {
        setX(getX() + velX);

        checkTilePos();
    }

    @Override
    public void render(Graphics g) {
        g.drawImage(tile, (int) getX(), (int) getY(), null);
    }

    public void checkTilePos() {
        if (getX() < -tile.getWidth()) {
            delete = true;
        }
    }
}
