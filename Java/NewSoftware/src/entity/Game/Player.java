package entity.Game;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.HashMap;

public class Player extends GameObject implements PlayerInterface {

    private double velX = 0;
    private double velY = 0;

    public boolean grounded;

    private BufferedImage player;

    public Player(double x, double y, HashMap<String, BufferedImage> playerSprites) {
        super(x, y);

        player = playerSprites.get("Idle");
    }

    @Override
    public void tick(Canvas canvas) {
        setX(getX() + velX);
        setY(getY() + velY);

        gravity();
        checkGround(canvas);
        resetPos(canvas);
    }

    @Override
    public void render(Graphics g) {
        g.drawImage(player, (int) getX(), (int) getY(), null);
    }

    public void setVelX(double velX) {
        this.velX = velX;
    }

    public void setVelY(double velY) {
        this.velY = velY;
    }

    public void gravity() {
        if (!grounded) {
            setY(getY() + 1);
        }
    }

    public void checkGround(Canvas canvas) {
        grounded = getY() >= (canvas.getHeight() - this.player.getHeight());
    }

    public void resetPos(Canvas canvas) {
        int xOffset = canvas.getWidth() - this.player.getWidth();
        int yOffset = canvas.getHeight() - this.player.getHeight();

        if (getX() < 0) setX(0);
        if (getX() > xOffset) setX(xOffset);

        if (getY() < 0) setY(0);
        if (grounded) setY(yOffset);
    }
}
