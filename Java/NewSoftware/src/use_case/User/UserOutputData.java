package use_case.User;

import entity.User;

public class UserOutputData {

    private final User user;

    private boolean useCaseFailed;

    public UserOutputData(User user) {
        this.user = user;
    }

    public User getUser() {
        return user;
    }

}
