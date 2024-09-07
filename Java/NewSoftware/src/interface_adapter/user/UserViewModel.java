package interface_adapter.user;

import entity.User;
import interface_adapter.Game.GameViewModel;
import interface_adapter.MainMenu.MainMenuViewModel;
import view.Game.GameView;
import view.ViewManager;
import view.ViewModel;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class UserViewModel extends ViewModel {

    private User loggedInUser;

    public final String PLACEHOLDER_BUTTON_STRING = "Placeholder Game";
    public final String MAINMENU_BUTTON_STRING = "Back To Main Menu";

    private GameViewModel gameViewModel;

    private UserState state = new UserState();

    public UserViewModel(ViewManager viewManager, GameViewModel gameViewModel)
    {
        super("User", viewManager);

        loggedInUser = null;
        this.gameViewModel = gameViewModel;
    }

    public UserState getState()
    {
        return state;
    }

    public void setState(UserState state)
    {
        this.state = state;
    }


    public User getLoggedInUser()
    {
        return loggedInUser;
    }

    public void setLoggedInUser(User loggedInUser)
    {
        this.loggedInUser = loggedInUser;
    }

    public GameViewModel getGameViewModel() { return this.gameViewModel; }

}
