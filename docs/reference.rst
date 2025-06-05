==========
Lua Module
==========

simNavground
============

.. lua:module:: simNavground

.. lua:function:: make_controller(int handle,string behavior,map kinematics,float radius)-> int handle

   Instantiate a navigation controller


   :param handle: A unique handle to associate to the controller
   :param behavior: The obstacle avoidance behavior
   :param kinematics: The kinematics
   :param radius: The radius

   :return: - **handle** -- The handle or -1 in case of failure
            



.. lua:function:: get_behavior_property(int handle,string name)-> map value

   Get the value of one of the navigation behavior properties


   :param handle: The controller handle
   :param name: The property name

   :return: - **value** -- The property value
            



.. lua:function:: set_behavior_property(int handle,string name,map value)

   Set the value of one of the navigation behavior properties


   :param handle: The controller handle
   :param name: The property name
   :param value: The property value




.. lua:function:: get_agents()-> int[] handles

   Get the handles of all the agents



   :return: - **handles** -- The handles
            



.. lua:function:: properties(int handle,int owner=-1)-> map[] properties

   Get all the agent properties


   :param handle: The agent handle
   :param owner: See `PropertyOwner`. Set to negative to get all properties

   :return: - **properties** -- The properties
            



.. lua:function:: _get_property(int handle,int owner,string name)-> map value

   Get the value of an agent's property


   :param handle: The agent handle
   :param owner: See `PropertyOwner`
   :param name: The property name

   :return: - **value** -- The property value
            



.. lua:function:: _set_property(int handle,int owner,string name,map value)

   Set the value of an agent's property


   :param handle: The agent handle
   :param owner: See `PropertyOwner`
   :param name: The property name
   :param value: The property value




.. lua:function:: set_lattice(int coordinate_index,float from,float to)

   TODO


   :param coordinate_index: TODO
   :param from: TODO
   :param to: TODO




.. lua:function:: get_lattice(int coordinate_index)-> bool enabled,float from,float to

   TODO


   :param coordinate_index: TODO

   :return: - **enabled** -- TODO
            - **from** -- TODO
            - **to** -- TODO
            



.. lua:function:: go_to_position(int handle,float[] position,float tolerance)

   TODO


   :param handle: The controller handle
   :param position: The target position
   :param tolerance: The target tolerance




.. lua:function:: go_to_pose(int handle,float[] position,float orientation,float position_tolerance,float orientation_tolerance)

   TODO


   :param handle: The controller handle
   :param position: The target position
   :param orientation: The target orientation
   :param position_tolerance: The target tolerance
   :param orientation_tolerance: The target tolerance




.. lua:function:: follow_point(int handle,float[] point)

   TODO


   :param handle: The controller handle
   :param point: The target position




.. lua:function:: follow_pose(int handle,float[] position,float orientation)

   TODO


   :param handle: The controller handle
   :param position: The target position
   :param orientation: The target orientation




.. lua:function:: get_target(int handle)-> map point

   TODO


   :param handle: The agent handle

   :return: - **point** -- The 2d target
            



.. lua:function:: get_pose(int handle)-> float[] position,float orientation

   TODO


   :param handle: The controller handle

   :return: - **position** -- The 3d position
            - **orientation** -- The orientation in radians
            



.. lua:function:: set_pose(int handle,float[] position,float orientation)

   TODO


   :param handle: The controller handle
   :param position: The 3d position
   :param orientation: The orientation in radians




.. lua:function:: get_twist(int handle)-> float[] velocity,float angular_speed

   TODO


   :param handle: The controller handle

   :return: - **velocity** -- The 2d velocity
            - **angular_speed** -- The angular speed in radians/s
            



.. lua:function:: set_twist(int handle,float[] velocity,float angular_speed)

   TODO


   :param handle: The controller handle
   :param velocity: The 3d velocity
   :param angular_speed: The angular speed in radians/s




.. lua:function:: set_rotation_tau(int handle,float value)

   TODO


   :param handle: The controller handle
   :param value: The value




.. lua:function:: set_horizon(int handle,float value)

   TODO


   :param handle: The controller handle
   :param value: The value




.. lua:function:: get_horizon(int handle)-> float value

   TODO


   :param handle: The controller handle

   :return: - **value** -- The value
            



.. lua:function:: set_safety_margin(int handle,float value)

   TODO


   :param handle: The controller handle
   :param value: The value




.. lua:function:: get_safety_margin(int handle)-> float value

   TODO


   :param handle: The controller handle

   :return: - **value** -- The value
            



.. lua:function:: set_optimal_speed(int handle,float value)

   TODO


   :param handle: The controller handle
   :param value: The value




.. lua:function:: get_optimal_speed(int handle)-> float value

   TODO


   :param handle: The controller handle

   :return: - **value** -- The value
            



.. lua:function:: set_heading_behavior(int handle,int value)

   TODO


   :param handle: The controller handle
   :param value: The value




.. lua:function:: set_speed_tolerance(int handle,float value)

   TODO


   :param handle: The controller handle
   :param value: The value




.. lua:function:: should_be_limited_to_2d(int handle,bool value)

   TODO


   :param handle: The controller handle
   :param value: The value




.. lua:function:: set_cmd_frame(int handle,int value)

   TODO


   :param handle: The controller handle
   :param value: The value (0 for relative, 1 for absolute)




.. lua:function:: follow_velocity(int handle,float[] velocity)

   TODO


   :param handle: The controller handle
   :param velocity: The target 3d velocity




.. lua:function:: update(int handle,float time_step)-> float[] velocity,float angular_speed,float state

   TODO


   :param handle: The controller handle
   :param time_step: The time step

   :return: - **velocity** -- The 3d velocity
            - **angular_speed** -- The angular speed in radians/s
            - **state** -- The angular speed in radians/s
            



.. lua:function:: set_static_obstacles(int handle,map[] obstacles)

   TODO


   :param handle: The controller handle
   :param obstacles: The controller handle




.. lua:function:: set_neighbors(int handle,map[] neighbors)

   TODO


   :param handle: The controller handle
   :param neighbors: The obstacles




.. lua:function:: set_line_obstacles(int handle,map[] obstacles)

   TODO


   :param handle: The controller handle
   :param obstacles: The lines




.. lua:function:: get_state(int handle)-> int state

   TODO


   :param handle: The controller handle

   :return: - **state** -- TODO
            



.. lua:function:: get_actuated_wheel_speeds(int handle)-> float[] speeds

   TODO


   :param handle: The controller handle

   :return: - **speeds** -- TODO
            



.. lua:function:: add_obstacle(int handle,float radius)

   TODO


   :param handle: The object handle
   :param radius: The object radius




.. lua:function:: add_wall(float[] p1,float[] p2)

   TODO


   :param p1: The first vertex
   :param p2: The second vertex




.. lua:function:: add_agent_from_yaml(int handle,string yaml)-> int handle

   TODO


   :param handle: The object handle
   :param yaml: The yaml text

   :return: - **handle** -- The handle or -1 in case of failure
            



.. lua:function:: remove_agent(int handle)

   TODO


   :param handle: The agent handle




.. lua:function:: get_last_cmd(int handle,int frame)-> float[] velocity,float angular_speed

   TODO


   :param handle: The agent handle
   :param frame: The value (0 for relative, 1 for absolute)

   :return: - **velocity** -- The horizontal velocity
            - **angular_speed** -- The angular speed in radians/s
            



.. lua:function:: get_last_wheel_cmd(int handle)-> float[] speeds

   TODO


   :param handle: The agent handle

   :return: - **speeds** -- TODO
            



.. lua:function:: enable_recording(map config)

   TODO


   :param config: The recording configuration




.. lua:function:: set_frame(int handle)

   Set the simulation reference frame.


   :param handle: The handle of the frame (-1 for use internal frame)



