package use_case.Game;

public interface GameInputBoundary {
    void save(GameOutputData data);
    void saveAndQuit(GameOutputData data);
}
