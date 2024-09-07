package interface_adapter.Options;

import java.awt.*;
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;

public class OptionsState {
    private final PropertyChangeSupport pcs = new PropertyChangeSupport(this);
    Dimension defaultRes;
    String defaultTheme;

    public OptionsState(Dimension size) {
        defaultRes = size;
        defaultTheme = "Default";
    }

    public Dimension getDefaultRes() { return defaultRes; }

    public String getDefaultTheme() { return defaultTheme; }

    public void addPropertyChangeListener(PropertyChangeListener listener) {
        this.pcs.addPropertyChangeListener(listener);
    }

    public void removePropertyChangeListener(PropertyChangeListener listener) {
        this.pcs.removePropertyChangeListener(listener);
    }
}
