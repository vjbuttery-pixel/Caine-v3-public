using UnityEngine;

namespace CaineBridge
{
    public static class CommandProcessor
    {
        public static void Process(string json)
        {
            try
            {
                CaineCommand command =
                    JsonUtility.FromJson<CaineCommand>(
                        json
                    );


                Debug.Log(
                    "[CAINE] Command received: "
                    + command.type
                );


                switch (command.type)
                {
                    case "CreateCircus":

                        SceneCreator.CreateMainCircus();

                        break;


                    case "CreateAdventure":

                        SceneCreator.CreateAdventure();

                        break;


                    case "SetWorld":

                        WorldManager.Instance.SetWorld(
                            command.payload.world,
                            WorldManager.WorldMode.Singleplayer
                        );
                    
                    

                        break;


                    default:

                        Debug.LogWarning(
                            "[CAINE] Unknown command: "
                            + command.type
                        );

                        break;

                    case "SpawnPrefab":

                        Vector3 position = Vector3.zero;

                        Quaternion rotation = Quaternion.identity;


                        if (command.payload.position != null)
                        {
                            position = new Vector3(
                                command.payload.position[0],
                                command.payload.position[1],
                                command.payload.position[2]
                            );
                        }


                        if (command.payload.rotation != null)
                        {
                            rotation = Quaternion.Euler(
                                command.payload.rotation[0],
                                command.payload.rotation[1],
                                command.payload.rotation[2]
                            );
                        }


                        AssetSpawner.Spawn(
                            command.payload.prefab,
                            position,
                            rotation
                        );

                        break;
                }

            }
            catch (System.Exception e)
            {
                Debug.LogError(
                    "[CAINE] Command error: "
                    + e.Message
                );
            }
        }
    }
}