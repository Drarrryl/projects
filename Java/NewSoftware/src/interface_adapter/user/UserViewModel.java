package interface_adapter.user;

import entity.User;
import view.ViewManager;
import view.ViewModel;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class UserViewModel extends ViewModel {

    private User loggedInUser;

    public UserViewModel(ViewManager viewManager)
    {
        super("Personal", viewManager);

        loggedInUser = null;
    }

    private UserState state = new UserState();

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

}