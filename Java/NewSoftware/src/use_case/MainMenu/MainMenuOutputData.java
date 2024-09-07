package use_case.MainMenu;

import entity.User;

public class MainMenuOutputData {
    private final String username;
    private final User user;

    public MainMenuOutputData(String username, User user) {
        this.username = username;
        this.user = user;
    }

    public String getUsername() {
        return username;
    }

    public User getUser() { return user; }
}
