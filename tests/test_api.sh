

ts=$(date +%s)


# user api
echo "\n------------- test api/create-user -------------"
curl "http://localhost/api/create-user?user_name=testname_$ts"

echo "\n------------- test api/get-all-users -------------"
curl "http://localhost/api/get-all-users"


# task api
echo "\n------------- test api/create-task -------------"
curl "http://localhost/api/create-task?task_title=mytask_$ts"

echo "\n------------- test api/get-all-tasks -------------"
curl "http://localhost/api/get-all-tasks"

echo "\n------------- test api/get-task-by-id -------------"
curl "http://localhost/api/get-task-by-id?task_id=96200489cc5a4ea6bfc73e94279500a4"


# vote api
echo "\n------------- test api/create-or-update-vote -------------"
curl "http://localhost/api/create-or-update-vote?user_id=userid_$ts&task_id=taskid_$ts&vote_variant=5"

echo "\n------------- test api/create-or-update-vote -------------"
curl "http://localhost/api/create-or-update-vote?user_id=userid_$ts&task_id=taskid_$ts&vote_variant=8"

echo "\n------------- test api/get-all-votes-by-task -------------"
curl "http://localhost/api/get-all-votes-by-task?task_id=taskid_$ts"


# vote_variant api
echo "\n------------- test api/get-available-vote-variants -------------"
curl "http://localhost/api/get-available-vote-variants"
