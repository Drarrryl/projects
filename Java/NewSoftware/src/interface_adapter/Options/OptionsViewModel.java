package interface_adapter.Options;

import entity.User;
import interface_adapter.user.UserViewModel;
import view.ViewManager;
import view.ViewModel;

public class OptionsViewModel extends ViewModel {

    public static final String TITLE_STRING = "Options";
    public static final String SET_RESOLUTION_STRING = "Set Resolution:";
    public static final String SET_THEME_STRING = "Set Theme:";
    public static final String BACK_BUTTON_STRING = "Back";
    public static final String RESET_TO_DEFAULT_BUTTON_STRING = "Reset to Default";

    private OptionsState optionsState;

    private User loggedInUser;

    public OptionsViewModel(ViewManager viewManager)
    {
        super("Options", viewManager);
        this.optionsState = new OptionsState(this.DEFAULT_SIZE);
        this.loggedInUser = null;
    }
    public OptionsState getState()
    {
        return optionsState;
    }

    public void setState(OptionsState state)
    {
        this.optionsState = state;
    }

    public User getLoggedInUser() { return loggedInUser; }

    public void setLoggedInUser(User loggedInUser)
    {
        this.loggedInUser = loggedInUser;
    }
}