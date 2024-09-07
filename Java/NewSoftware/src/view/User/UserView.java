package view.User;

import interface_adapter.user.UserController;
import interface_adapter.user.UserViewModel;
import view.View;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UserView extends View {
    final private UserController userController;

    private JButton mainMenuButton;
    private JButton placeholderGameButton;
    public UserView(UserViewModel userViewModel, UserController userController) {
        super(userViewModel);
        this.userController = userController;

        JPanel titlePanel = new JPanel();

        JPanel buttonPanel = new JPanel();
        mainMenuButton = new JButton(userViewModel.MAINMENU_BUTTON_STRING);
        placeholderGameButton = new JButton(userViewModel.PLACEHOLDER_BUTTON_STRING);
        buttonPanel.add(mainMenuButton);
        buttonPanel.add(placeholderGameButton);
        buttonPanel.setLayout(new BoxLayout(buttonPanel, BoxLayout.X_AXIS));

        mainMenuButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                userController.mainMenu();
            }
        });

        placeholderGameButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                userController.startGame(userViewModel.getLoggedInUser());
            }
        });

        this.add(titlePanel);
        this.add(buttonPanel);
        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        userViewModel.SetTheme(this, userViewModel.getViewManager().getTheme());
    }
}
