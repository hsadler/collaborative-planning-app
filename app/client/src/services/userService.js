
const UserService = {}

UserService.user = null

UserService.setUser = (user) => {
	UserService.user = user
}

UserService.getUser = () => {
	return UserService.user
}

export default UserService
