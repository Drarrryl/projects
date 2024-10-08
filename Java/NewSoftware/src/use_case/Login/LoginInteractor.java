package use_case.Login;

import data_access.DataAccessInterface;
import entity.User;

public class LoginInteractor implements LoginInputBoundary {
    final DataAccessInterface userDataAccessObject;
    final LoginOutputBoundary loginPresenter;

    public LoginInteractor(DataAccessInterface userDataAccessInterface,
                           LoginOutputBoundary loginOutputBoundary) {
        this.userDataAccessObject = userDataAccessInterface;
        this.loginPresenter = loginOutputBoundary;
    }

    @Override
    public void execute(LoginInputData loginInputData) {
        String username = loginInputData.getUsername();
        String password = loginInputData.getPassword();
        if (username.isBlank()) {
            loginPresenter.prepareFailView("Invalid Username!");
        } else if (password.isBlank()) {
            loginPresenter.prepareFailView("Invalid Password!");
        } else if (userDataAccessObject.readUser(username) == null) {
            loginPresenter.prepareFailView(username + ": Account does not exist.");
        } else {
            String pwd = userDataAccessObject.readUser(username).getPassword();
            if (!password.equals(pwd)) {
                loginPresenter.prepareFailView("Incorrect password for " + username + ".");
            } else {

                User user = userDataAccessObject.readUser(loginInputData.getUsername());

                LoginOutputData loginOutputData = new LoginOutputData(user.getUsername(), user, false);
                loginPresenter.prepareSuccessView(loginOutputData);
            }
        }
    }
}
