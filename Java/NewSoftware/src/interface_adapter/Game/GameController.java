package interface_adapter.Game;

import entity.Game.GameObject;
import entity.Game.Player;
import use_case.Game.GameInputBoundary;
import use_case.User.UserInputBoundary;
import use_case.User.UserInputData;

import java.awt.*;
import java.awt.event.KeyEvent;
import java.time.LocalDateTime;
import java.util.ArrayList;

public class GameController {

    private ArrayList<GameObject> objects = new ArrayList<>();
    private final GameInputBoundary gameInteractor;

    public GameController(GameInputBoundary gameInputBoundary)
    {
        this.gameInteractor = gameInputBoundary;
    }

    public void keyPressed(int keyCode, Player plr) {
        if (keyCode == KeyEvent.VK_W) {
            plr.setVelY(-5);
        } else if (keyCode == KeyEvent.VK_S) {
            if (!plr.grounded) plr.setVelY(5);
        } else if (keyCode == KeyEvent.VK_A) {
            plr.setVelX(-5);
        } else if (keyCode == KeyEvent.VK_D) {
            plr.setVelX(5);
        }
    }

    public void keyReleased(int keyCode, Player plr) {
        if (keyCode == KeyEvent.VK_W) {
            plr.setVelY(0);
        } else if (keyCode == KeyEvent.VK_S) {
            plr.setVelY(0);
        } else if (keyCode == KeyEvent.VK_A) {
            plr.setVelX(0);
        } else if (keyCode == KeyEvent.VK_D) {
            plr.setVelX(0);
        }
    }

    public void addObj(GameObject obj) {
        objects.add(obj);
    }

    public void removeObj(GameObject obj) {
        objects.remove(obj);
    }

    public void tick(Canvas gameCanvas) {
        for (GameObject obj : objects) {
            obj.tick(gameCanvas);
        }
    }

    public void render(Graphics g) {
        for (GameObject obj : objects) {
            obj.render(g);
        }
    }

    public void exitGame() {
        gameInteractor.saveAndQuit();
    }
}
