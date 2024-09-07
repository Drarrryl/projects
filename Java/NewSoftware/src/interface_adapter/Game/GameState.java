package interface_adapter.Game;

import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;

public class GameState {
    private final PropertyChangeSupport pcs = new PropertyChangeSupport(this);
    private String username;
    private int highScore;
    private int numberOfAttempts;
    private boolean status;

    public GameState() {}

    public String getUsername() {
        return this.username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public boolean getStatus() {
        return this.status;
    }

    public void setStatus(boolean status) {
        boolean oldStatus = this.status;
        this.status = status;
        pcs.firePropertyChange("status", oldStatus, status);
    }

    public void addPropertyChangeListener(PropertyChangeListener listener) {
        this.pcs.addPropertyChangeListener(listener);
    }

    public void removePropertyChangeListener(PropertyChangeListener listener) {
        this.pcs.removePropertyChangeListener(listener);
    }
}
