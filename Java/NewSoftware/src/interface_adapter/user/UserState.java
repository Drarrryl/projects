package interface_adapter.user;

import java.time.LocalDateTime;

public class UserState {

    private String username;

    public UserState() {}

    public String getUsername() {
        return this.username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
}
