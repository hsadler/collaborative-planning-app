
const UserService = {}

UserService.user = null

UserService.setUser = (user) => {
	UserService.user = user
	localStorage.setItem('user', JSON.stringify(user))
}

UserService.getUser = () => {
	return UserService.user
}

export default UserService
