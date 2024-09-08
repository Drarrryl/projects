package entity.Game;

import java.awt.*;

public interface Collidable {
    public Rectangle getBounds();
    public void tick(Canvas canvas);
    public void render(Graphics g);
}
