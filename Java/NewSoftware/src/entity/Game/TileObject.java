package entity.Game;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.HashMap;

public class TileObject extends GameObject {

    private BufferedImage tile;
    private BufferedImage spikes;
    public TileObject(double x, double y, HashMap<String, BufferedImage> tileSprites) {
        super(x, y);

        tile = tileSprites.get("Grass");
        spikes = tileSprites.get("Spikes");
    }

    @Override
    public void tick(Canvas gameCanvas) {

    }

    @Override
    public void render(Graphics g) {
        g.drawImage(tile, (int) getX(), (int) getY(), null);
    }
}
