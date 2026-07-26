using System.Collections.Generic;
using UnityEngine;

namespace CaineBridge
{
    public class PlayerManager : MonoBehaviour
    {
        public static PlayerManager Instance;


        private readonly Dictionary<string, PlayerData> players = new();


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


        public void RegisterPlayer(PlayerData player)
        {
            if (player == null)
                return;


            players[player.Id] = player;


            Debug.Log(
                "[CAINE] Player registered: "
                + player.Name
            );
        }


        public void RemovePlayer(string id)
        {
            if (players.ContainsKey(id))
            {
                players.Remove(id);


                Debug.Log(
                    "[CAINE] Player removed: "
                    + id
                );
            }
        }


        public PlayerData GetPlayer(string id)
        {
            players.TryGetValue(
                id,
                out PlayerData player
            );

            return player;
        }


        public IEnumerable<PlayerData> GetAllPlayers()
        {
            return players.Values;
        }


        public int PlayerCount()
        {
            return players.Count;
        }
    }
}