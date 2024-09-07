package interface_adapter.Game;

import use_case.Game.GameOutputBoundary;
import use_case.Game.GameOutputData;
import use_case.User.UserOutputBoundary;
import use_case.User.UserOutputData;
import view.ViewManager;

public class GamePresenter implements GameOutputBoundary
{
    ViewManager viewManager;
    GameViewModel gameViewModel;

    public GamePresenter(ViewManager viewManager, GameViewModel gameViewModel)
    {
        this.viewManager = viewManager;
        this.gameViewModel = gameViewModel;
    }

    @Override
    public void prepareWinView() {

    }

    @Override
    public void prepareLoseView() {

    }

    @Override
    public void prepareSaveAndQuit() {
        viewManager.switchToLastView();
        viewManager.setResolution(viewManager.getLastViewModel().DEFAULT_SIZE);
    }
}
