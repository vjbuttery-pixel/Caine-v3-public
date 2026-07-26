using UnityEngine;

namespace CaineBridge
{
    public class WorldSessionManager : MonoBehaviour
    {
        public static WorldSessionManager Instance;


        private bool worldRunning;


        private void Awake()
        {
            if (Instance == null)
            {
                Instance = this;

                DontDestroyOnLoad(gameObject);
            }
            else
            {
                Destroy(gameObject);
            }
        }


        public void ResumeWorld()
        {
            if (worldRunning)
                return;


            worldRunning = true;


            Debug.Log(
                "[CAINE] World session resumed"
            );


            StartWorldSystems();
        }


        public void PauseWorld()
        {
            if (!worldRunning)
                return;


            worldRunning = false;


            Debug.Log(
                "[CAINE] World session paused"
            );


            StopWorldSystems();
        }


        private void StartWorldSystems()
        {
            /*
             Later this will activate:

             - Caine thinking
             - Resident AI
             - Weather
             - Time
             - Events
             - Simulation
            */


            Debug.Log(
                "[CAINE] Simulation started"
            );
        }


        private void StopWorldSystems()
        {
            /*
             Later this will pause:

             - Caine thinking
             - Resident AI
             - Weather
             - Time
             - Events
             - Simulation
            */


            Debug.Log(
                "[CAINE] Simulation stopped"
            );
        }


        public bool IsWorldActive()
        {
            return worldRunning;
        }
    }
}