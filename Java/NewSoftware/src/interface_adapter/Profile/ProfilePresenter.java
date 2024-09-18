package interface_adapter.Profile;

import use_case.Profile.ProfileOutputBoundary;
import view.ViewManager;

public class ProfilePresenter implements ProfileOutputBoundary {
    private ViewManager viewManager;
    private ProfileViewModel profileViewModel;

    public ProfilePresenter(ViewManager viewManager, ProfileViewModel profileViewModel) {
        this.viewManager = viewManager;
        this.profileViewModel = profileViewModel;
    }
}
