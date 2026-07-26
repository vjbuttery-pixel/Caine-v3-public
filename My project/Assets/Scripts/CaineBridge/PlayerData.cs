using System;

namespace CaineBridge
{
    [Serializable]
    public class PlayerData
    {
        public string Id;

        public string Name;

        public string CurrentRoom;

        public bool Connected;

        public string AvatarId;

        public string Mood;

        public string CurrentActivity;

        public string CurrentAdventure;

        public string Inventory;

        public string Personality;

        public string VoiceProfile;
    }
}