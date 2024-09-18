package interface_adapter.Profile;

import entity.User;
import interface_adapter.State;

import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;

public class ProfileState implements State {
    private final PropertyChangeSupport pcs = new PropertyChangeSupport(this);
    private User loggedInUser;

    public ProfileState() {

    }

    public User getLoggedInUser() {
        return loggedInUser;
    }

    public void setLoggedInUser(User loggedInUser) {
        this.loggedInUser = loggedInUser;
    }

    @Override
    public String getUsername() {
        return null;
    }

    @Override
    public long getHighscore() {
        return 0;
    }

    public void addPropertyChangeListener(PropertyChangeListener listener) {
        this.pcs.addPropertyChangeListener(listener);
    }

    public void removePropertyChangeListener(PropertyChangeListener listener) {
        this.pcs.removePropertyChangeListener(listener);
    }
}
