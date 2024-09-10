package interface_adapter.Game;

import entity.User;
import view.ViewManager;
import view.ViewModel;

public class GameViewModel extends ViewModel {

    private User loggedInUser;

    public String TITLE = "Placeholder Game";
    public String START_GAME_BUTTON = "Start Game";
    public String EXIT_GAME_BUTTON = "Exit Game";

    public GameViewModel(ViewManager viewManager)
    {
        super("Game", viewManager);

        loggedInUser = null;
    }

    private GameState state = new GameState();

    public GameState getState()
    {
        return state;
    }

    public void setState(GameState state)
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

}
