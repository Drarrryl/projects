package interface_adapter.Profile;

import view.ViewManager;
import view.ViewModel;

public class ProfileViewModel extends ViewModel {
    private ProfileState state = new ProfileState();
    public ProfileViewModel(ViewManager viewManager) {
        super("Profile", viewManager);
    }

    public ProfileState getProfileState() {
        return state;
    }
}
