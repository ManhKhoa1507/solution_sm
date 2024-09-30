variable "github_token" {
  description = "GitHub token with access to manage teams"
  type        = string
}

variable "github_org" {
  description = "GitHub organization or user name"
  type        = string
  default     = "H4desOrg"
}

# User roles across teams: map of users and their team roles
variable "team_member" {
  type = map(list(string))
  default = {
    team1 = [
      "User1",
      "User2",
      "User3",
      "User5",
      "User6",
      "User7",
      "User8",
      "User9",
      "User10",
    ]
    team2 = [
      "User1",
      "User2",
      "User3",
      "User4",
      "User6",
      "User7",
      "User8",
      "User9",
      "User10",
    ]
    team3 = [
      "User1",
      "User2",
      "User3",
      "User4",
      "User5",
      "User6",
      "User7",
    ]
    team4 = [
      "User1",
      "User2",
      "User3",
      "User4",
      "User5",
      "User6",
      "User7",
      "User8",
      "User9",
      "User10",
    ]
    team5 = [
      "User1",
      "User2",
      "User3",
      "User4",
      "User6",
      "User7",
      "User8",
      "User9",
      "User10",
    ]
    team6 = [
      "User1",
      "User2",
      "User3",
      "User4",
      "User5",
      "User7",
      "User8",
      "User9",
      "User10",
    ]
  }
}

variable "github_users" {
  type = list(object({
    username = string
    email    = string
  }))
  default = [
    { username = "User1", email = "user1@example.com" },
    { username = "User2", email = "user2@example.com" },
    { username = "User3", email = "user3@example.com" },
    { username = "User4", email = "user4@example.com" },
    { username = "User5", email = "user5@example.com" },
    { username = "User6", email = "user6@example.com" },
    { username = "User7", email = "user7@example.com" },
    { username = "User8", email = "user8@example.com" },
    { username = "User9", email = "user9@example.com" },
    { username = "User10", email = "user10@example.com" }
  ]
}
