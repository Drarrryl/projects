package use_case.Game;

import data_access.DataAccessInterface;
import entity.User;
import use_case.Game.GameOutputBoundary;

public class GameInteractor implements GameInputBoundary {
    final DataAccessInterface gameDataAccessObject;
    final GameOutputBoundary gamePresenter;
    public GameInteractor(DataAccessInterface gameDataAccessInterface,
                          GameOutputBoundary gameOutputBoundary) {
        this.gameDataAccessObject = gameDataAccessInterface;
        this.gamePresenter = gameOutputBoundary;
    }

    public void saveAndQuit(GameOutputData outputData) {
        long score = outputData.getScore();
        User user = outputData.getUser();

        System.out.println("Current Score: " + score + " User Highscore: " + user.getHighscore());

        if (score > user.getHighscore()) {
            gameDataAccessObject.updateHighscore(user, score);
        }
        gamePresenter.prepareSaveAndQuit();
    }
}
