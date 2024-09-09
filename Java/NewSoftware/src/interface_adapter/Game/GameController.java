package interface_adapter.Game;

import entity.Game.*;
import org.checkerframework.checker.units.qual.A;
import use_case.Game.GameInputBoundary;
import use_case.User.UserInputBoundary;
import use_case.User.UserInputData;
import view.Game.GameView;

import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.image.BufferedImage;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public class GameController {

    private ArrayList<Collidable> collidableObjs = new ArrayList<>();
    private ArrayList<NonCollidable> nonCollidableObjs = new ArrayList<>();
    private final GameInputBoundary gameInteractor;

    public GameController(GameInputBoundary gameInputBoundary)
    {
        this.gameInteractor = gameInputBoundary;
    }

    public void keyPressed(int keyCode, Player plr) {
        if (keyCode == KeyEvent.VK_W) {
            if (plr.grounded) plr.jump();
        } else if (keyCode == KeyEvent.VK_S) {
            if (!plr.grounded) plr.setVelY(5);
        } else if (keyCode == KeyEvent.VK_A) {
            plr.setVelX(-5);
        } else if (keyCode == KeyEvent.VK_D) {
            plr.setVelX(5);
        }
    }

    public void keyReleased(int keyCode, Player plr) {
        if (keyCode == KeyEvent.VK_S) {
            plr.setVelY(0);
        } else if (keyCode == KeyEvent.VK_A) {
            plr.setVelX(0);
        } else if (keyCode == KeyEvent.VK_D) {
            plr.setVelX(0);
        }
    }

    public void addObj(Collidable obj) {
        collidableObjs.add(obj);
    }

    public void removeObj(Collidable obj) {
        collidableObjs.remove(obj);
    }

    public void addObj(NonCollidable obj) {
        nonCollidableObjs.add(obj);
    }

    public void removeObj(NonCollidable obj) {
        nonCollidableObjs.remove(obj);
    }

    public void tick(Canvas gameCanvas, HashMap<String, BufferedImage> tileSprites) {
        for (Collidable obj : collidableObjs) {
            obj.tick(gameCanvas);
        }

        for (NonCollidable obj : nonCollidableObjs) {
            obj.tick(gameCanvas, this);
        }

        updateTile(tileSprites);
    }

    public void render(Graphics g) {
        for (Collidable obj : collidableObjs) {
            obj.render(g);
        }

        for (NonCollidable obj : nonCollidableObjs) {
            obj.render(g);
        }
    }

    public ArrayList<Collidable> getCollidableObjs() {
        return collidableObjs;
    }

    public ArrayList<NonCollidable> getNonCollidableObjs() {
        return nonCollidableObjs;
    }

    public void updateTile(HashMap<String, BufferedImage> tileSprites) {
        for (int i = 0; i < collidableObjs.size(); i++) {
            Collidable currObj = collidableObjs.get(i);

            if (currObj instanceof TileObject) {
                if (((TileObject) currObj).delete) {
                    removeObj(currObj);
                    TileObject tailTile = findTailTile();
                    double x = tailTile.getX() + tailTile.getWidth();
                    double y = tailTile.getY();
                    Random r = new Random();

                    addObj(new TileObject(x, y, tileSprites, r.nextBoolean()));
                }
            }
        }
    }

    private TileObject findTailTile() {
        TileObject resultObj = null;

        for (int i = 0; i < collidableObjs.size(); i++) {
            Collidable currObj = collidableObjs.get(i);

            if (currObj instanceof TileObject) {
                if (resultObj == null) {
                    resultObj = (TileObject) currObj;
                } else if (((TileObject) currObj).getX() > resultObj.getX()) {
                    resultObj = (TileObject) currObj;
                }
            }
        }
        return resultObj;
    }

    public void exitGame() {
        gameInteractor.saveAndQuit();
    }
}
