package interface_adapter.Login;

import use_case.Login.LoginOutputBoundary;
import use_case.Login.LoginOutputData;
import view.ViewManager;

public class LoginPresenter implements LoginOutputBoundary {

    private LoginViewModel loginViewModel;
    private ViewManager viewManager;

    public LoginPresenter(ViewManager viewManager, LoginViewModel loginViewModel)
    {
        this.loginViewModel = loginViewModel;
        this.viewManager = viewManager;
    }


    @Override
    public void prepareSuccessView(LoginOutputData user) {
        loginViewModel.getState().setUsername(user.getUsername());
        viewManager.switchToView(loginViewModel.getMainMenuViewModel().getName());
        loginViewModel.getMainMenuViewModel().setLoggedInUser(user.getUser());
    }

    @Override
    public void prepareFailView(String error) {
        loginViewModel.getState().setUsernameError(error);
        viewManager.showErrorMessage(error);
    }
}