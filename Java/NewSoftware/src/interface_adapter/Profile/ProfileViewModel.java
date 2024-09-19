package interface_adapter.Profile;

import view.ViewManager;
import view.ViewModel;

public class ProfileViewModel extends ViewModel {
    public final String BACK_BUTTON_STRING = "Back";
    private ProfileState state = new ProfileState();
    public ProfileViewModel(ViewManager viewManager) {
        super("Profile", viewManager);
    }

    public ProfileState getProfileState() {
        return state;
    }
}
