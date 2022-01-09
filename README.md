 #                                                Pokemon Game

<img src="https://user-images.githubusercontent.com/69717074/148642755-15047593-9988-4efb-932d-91ac4def50d8.png" width="450">

## About the project

In this project , we programmed a pokemon game which was based on directed weighted graph. The game, was programmed by Python. 

## Classes and methods 

The part of the project was based on the previous task. So we used 3 previous classes.

## DiGraph - We will detail the class and what each function does :

We created a constructor, which gets the number of vertices, the number of sides, a counter, and a dictionary of vertices that will contain in the key the ID of the vertex and in value the information about the vertex.

|Function name | Explanation |
|--------------|-------------|
| v_size | Function returns the number of vertices in the graph |
| e_size | Returns the number of sides in the graph |
| get_all_v | A function that returns to us the dictionary of vertices that contains all the information |
| all_in_edges_of_node | A function that returns a dictionary, where in this key the ID of the vertex and value is all the vertices connected to it (if there is one) |
| all_out_edges_of_node | A function like the previous one, only it returns the vertices that come out of a vertex |
| get_mc | A function by which we count every change we make in the construction of the graph, such as adding a side, deleting a side, adding a vertex, etc. |
| add_edge | A function that adds a side to a graph, since we did not have a side object but only a vertex, we had to work with both dictionaries and vertex objects that could simulate us sides. So when adding a edge we had to put the source in the inEdges dictionary and the destination in the outEdges and coordinate between them. |
| add_node | A function that adds a vertex to a graph |
| remove_node | A function that deletes the vertex from the grap . |
| remove_edge | A function that deletes the side, that is, deletes them from both dictionaries the source and the destination. And print functions. |

## GraphAlgo class that contains algorithms:

Contains the constructor that builds the graph through the DiGraph class

|Function name | Explanation |
|--------------|-------------|
| get_ graph | A function that returns the graph |
| load_from_dict | A function that loads a dictionary and converts it to an object |
| save_to_json  | A function that saves us the graph for a new json file. In its operation each time overwrites the previous file. |
| shortest_path | A function that calculates for us the shortest route from source vertex to destination vertex. We used the dijkstra algorithm which is detailed below. |
| tsp | A function that calculates for us the shortest path to pass between all vertices, we used it in the FloydWarshall algorithm which we will explain later. |
| center | A function that calculates the most central vertex, from which the other vertices can be reached in the "cheapest" way. |
| plot_graph | A function that emits the graph (was not used in this task) |


## Node

Also we created Node class, that holds node object.
There is a constructor that gets id, pos, tag, weight, inEdges, outEdges
Since we did not have an edge object, we used vertex information with the dictionaries.
pos , tag and weight - have default values in the constructor.



 # Explanation of the algorithm 
 
 In our algorithm , we are mostly using the center and shortest path algorithms.
 At first we put the agents on the center node , because we know , that from this vertex there is the shortest way to get to the rest of the vertices . Then , we are pass in for loop throw all the agents we have and calculates the paths to the pokemons by the shortest path algorithm from the src of the agent to pokemon src/dest ( it depends on whether a Pokemon is on a rising or falling edge). The shortest path returns us the cost of the path and the path itself , we are checking by the cost function if the path is the cheapest or not and moving by the path that was returned for us from the shortest path function. Pokemon that is on up edge has a Red color and pokemon that on down edge has a blue color. 

## Client 
The client class includes functions that connect with the server , each function in it ,when using it , sends a message to a server and executes the commands of a game.

|Function name | Explanation |
|--------------|-------------|
| start_connection | the function that start connection with a server while you execute it |
| send_message | the function that sends messages with commands to a server |
| get_agents | return the agents that are on the graph (return a dictionary with string) |
| add_agent | add an agent to game that start on some node|
| get_graph | function that returns us a graph of specific scenario |
| get_info | function that returns us the information about the game |
| get_pokemons | function that returns us exactly pokemons we are working on now |
| is_running | function that returns us true if the game is still running ,false if not |
| time to end | returns us the time to the end of the game |
| start | begins the game |
| stop | stop the game and reports to server |
| stop_connection | stops the connection with the server |
| log_in | function that allows us to log in with our id and report about the cases |
| choose_next_edge | function there we write there  the next node, the agent will move to |
| move | function thet makes a move for agent |


## Student_code 

|Function name | Explanation |
|--------------|-------------|
| min_x,min_y,max_x,max_y | we made these funcions , for the resolution of the screen ,we took the highest point and the lowest point of the graph , for the ability to make a "zoom in " on the screen because the coordinates of the points were too near to each other |
| scale , my_scale | these functions have a formula fr the resolution, there we used the highest and the lowest points |
| load_from_pokemon_dict | the function that load the pokemns from a dictionary and converts them to the pokemn object |
| load_from_agent_dict | exactle the same function that load from a dictionary and convert to the agent object |


## Button class 
The class is creating an bject of button, it includes only constructor and press function, which will stop the game in every moment.

## Cost class

|Function name | Explanation |
|--------------|-------------|
| line | the function that cheks on which edge exactly the pokemon is and returns us the src and the dest of this edge |
| cost | this function checks ,which path will be the cheapest for the agent to go to come pokemon and return the cost |
 
 Also we signed in different colors , different pokemons and signed different agents by their own id numbers.
 
 ## pokimon class 
 
 In this class we created pokemon object , the class includes only constructor and __str__ and __repr__ functions.
 
 ## agent class
 
 In this class, like the pokimon class , we created an agent object , this class also includes only constructor ans __str__ , __repr__ functions 
 
 Also we added to our GUI picture of pokimon ,timer for the game and the stop button that will stop the game in every moment you will decide to stop it .
 
 ## Tests 
 We made a test for the classes , you can check in "Tests" directory .
 
 You can run our algorithm with the release , we made for you.
 
 ## Uml Diagram
 
![GraphAlgo](https://user-images.githubusercontent.com/69717074/148691023-2293609e-8308-454c-b1d5-0c32db761ca2.png)

 



