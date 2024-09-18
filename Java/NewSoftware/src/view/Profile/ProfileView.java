package view.Profile;

import interface_adapter.Profile.ProfileController;
import interface_adapter.Profile.ProfileViewModel;
import view.User.ProfilePanel;
import view.View;

public class ProfileView extends View {

    private ProfileController controller;

    private SignupView signupView;

    public ProfileView(ProfileViewModel viewModel, ProfileController controller) {
        super(viewModel);
        this.controller = controller;

        //ProfilePanel profilePanel = new ProfilePanel(viewModel.getProfileState().getLoggedInUser(), viewModel);
    }
}
