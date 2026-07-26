using UnityEngine;

namespace CaineBridge
{
    public class BridgeStartup : MonoBehaviour
    {
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)]
        static void Initialise()
        {
            GameObject bridge = new GameObject("Caine Bridge");

            bridge.AddComponent<UnityBridge>();
            bridge.AddComponent<NetworkListener>();
            bridge.AddComponent<WorldManager>();
            bridge.AddComponent<SaveSystem>();
            bridge.AddComponent<PrefabRegistry>();
            bridge.AddComponent<WorldSessionManager>();
            bridge.AddComponent<PlayerManager>();
            bridge.AddComponent<ResidentManager>();

            DontDestroyOnLoad(bridge);
        }
    }
}