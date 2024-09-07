package use_case.Game;

import data_access.DataAccessInterface;
import use_case.Game.GameOutputBoundary;

public class GameInteractor implements GameInputBoundary {
    final DataAccessInterface gameDataAccessObject;
    final GameOutputBoundary gamePresenter;
    public GameInteractor(DataAccessInterface gameDataAccessInterface,
                          GameOutputBoundary gameOutputBoundary) {
        this.gameDataAccessObject = gameDataAccessInterface;
        this.gamePresenter = gameOutputBoundary;
    }

    public void saveAndQuit() {
        gamePresenter.prepareSaveAndQuit();
    }
}
