package use_case.User;

public interface UserOutputBoundary {
    void prepareStartView(UserOutputData user);
    void prepareMainMenuView();

    void prepareFailView(String error);
}
