package interface_adapter.user;

import interface_adapter.Game.GameViewModel;
import interface_adapter.MainMenu.MainMenuViewModel;
import use_case.User.UserOutputBoundary;
import use_case.User.UserOutputData;
import view.ViewManager;

import javax.swing.*;

public class UserPresenter implements UserOutputBoundary
{
    ViewManager viewManager;
    UserViewModel userViewModel;

    public UserPresenter(ViewManager viewManager, UserViewModel userViewModel)
    {
        this.viewManager = viewManager;
        this.userViewModel = userViewModel;
    }

    @Override
    public void prepareStartView(UserOutputData user) {
        GameViewModel gameViewModel = userViewModel.getGameViewModel();
        viewManager.switchToView(gameViewModel.getName());
        viewManager.setResolution(gameViewModel.DEFAULT_SIZE);
        gameViewModel.setLoggedInUser(user.getUser());
        gameViewModel.getState().setUsername(user.getUser().getUsername());
        gameViewModel.getState().setStatus(true);
    }

    @Override
    public void prepareMainMenuView() {
        MainMenuViewModel mainMenuViewModel = (MainMenuViewModel) userViewModel.getViewManager().getViewModel("Main Menu");
        viewManager.switchToView(mainMenuViewModel.getName());
        viewManager.setResolution(mainMenuViewModel.DEFAULT_SIZE);
    }

    @Override
    public void prepareFailView(String error) {
        viewManager.showErrorMessage(error);
        viewManager.closeView();
    }
}
