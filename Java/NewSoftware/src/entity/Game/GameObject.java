package entity.Game;

import java.awt.*;

public class GameObject implements GameObjectInterface {

    private double x;
    private double y;

    public GameObject(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }

    @Override
    public void tick(Canvas gameCanvas) {

    }

    @Override
    public void render(Graphics g) {

    }
}
