- mi ./app.js  
	''' import React from 'react';

	import { Provider } from 'react-redux';
	
	import { PersistGate } from 'redux-persist/integration/react';
	
	import 'react-native-gesture-handler';
	
	import Navigation from './Navigation';
	
	import { store, persistor } from './app/redux/Store';
	
	  
	
	export default function App() {
	
	  return (
	
	    <Provider store={store}>
	
	      <PersistGate loading={null} persistor={persistor}>
	
	        <Navigation />
	
	      </PersistGate>
	
	    </Provider>
	
	  );
	
	}''' 
- mi ./app/redux/Store.js
	- // store.js
	
	import { configureStore } from '@reduxjs/toolkit';
	
	import AsyncStorage from '@react-native-async-storage/async-storage';
	
	import { persistReducer, persistStore } from 'redux-persist';
	
	import userReducer from '../redux/slices/User';
	
	  
	
	const persistConfig = {
	
	  key: 'root',
	
	  storage: AsyncStorage,
	
	};
	
	  
	
	const persistedReducer = persistReducer(persistConfig, userReducer);
	
	  
	
	const store = configureStore({
	
	  reducer: persistedReducer,
	
	});
	
	  
	
	let persistor = persistStore(store);
	
	  
	
	export { store, persistor };
- mi ./test.js  
	- import React, { useState } from 'react';

	import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
	
	import { useSelector, useDispatch } from 'react-redux';
	
	import { setUser } from './app/redux/slices/User';
	
	  
	
	const UserScreen = () => {
	
	    const dispatch = useDispatch();
	
	    const currentUser = useSelector(state => state.user.currentUser);
	
	    const [newUserName, setNewUserName] = useState('');
	
	    const handleUserChange = () => {
	
	      dispatch(setUser({ name: newUserName }));
	
	      setNewUserName('');
	
	    };
	
	    return (
	
	      <View style={styles.container}>
	
	        <Text style={styles.title}>User Screen</Text>
	
	        {currentUser ? (
	
	          <View>
	
	            <Text style={styles.text}>Current User: {currentUser.name}</Text>
	
	          </View>
	
	        ) : (
	
	          <Text style={styles.text}>No user selected</Text>
	
	        )}
	
	        <TextInput
	
	          style={styles.input}
	
	          placeholder="Enter new user name"
	
	          value={newUserName}
	
	          onChangeText={setNewUserName}
	
	        />
	
	        <Button title="Set User" onPress={handleUserChange} />
	
	      </View>
	
	    );
	
	  };
	
	  
	
	const styles = StyleSheet.create({
	
	  container: {
	
	    flex: 1,
	
	    alignItems: 'center',
	
	    justifyContent: 'center',
	
	    padding: 20,
	
	  },
	
	  title: {
	
	    fontSize: 24,
	
	    marginBottom: 20,
	
	  },
	
	  text: {
	
	    fontSize: 18,
	
	    marginBottom: 10,
	
	  },
	
	  input: {
	
	    borderWidth: 1,
	
	    borderColor: '#ccc',
	
	    padding: 10,
	
	    width: '80%',
	
	    marginBottom: 10,
	
	  },
	
	});
	
	  
	
	export default UserScreen;
- mi ./Navigation.js
	import { NavigationContainer } from "@react-navigation/native";

	import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
	
	import {  createNativeStackNavigator } from "@react-navigation/native-stack";
	
	import Feed from "./screens/tabScreens/Feed";
	
	import Notifications from "./screens/tabScreens/Notifications";
	
	import ProductListStackNavigator from "./screens/tabScreens/Settings";
	
	import SignInScreen from "./screens/SignInScreen";
	
	import { AntDesign } from '@expo/vector-icons';
	
	import DetailScreen from "./components/DetailScreen";
	
	import ComisionistaDetails from "./components/ComisionistaDetails";
	
	import Productos from "./Productos";
	
	import UserTest from "./test"
	
	  
	
	const Stack = createNativeStackNavigator();
	
	const FeedStack = () => {
	
	    return (
	
	      <Stack.Navigator>
	
	        <Stack.Screen name="Clientes" component={Feed}  />
	
	        <Stack.Screen component={Productos} name="ClientDetails" options={{ title: "Detalles Cliente", presentation: "modal" }} />
	
	      </Stack.Navigator>
	
	    );
	
	  };
	
	  
	
	const Tab2Stack = () => {
	
	    return (
	
	        <Stack.Navigator>
	
	            <Stack.Screen name = "Productos" component={ProductListStackNavigator} />
	
	            <Stack.Screen name = "ProductDetails" component={UserTest} options={{title: "Detalles Producto", presentation: "modal"  }}/>
	
	        </Stack.Navigator>
	
	    );
	
	};
	
	  
	
	const Tab3Stack = () => {
	
	    return (
	
	        <Stack.Navigator>
	
	            <Stack.Screen name = "Comisionistas" component={Notifications} />
	
	            <Stack.Screen name = "ComisionistaDetails" component={ComisionistaDetails} options={{title: "Detalles Comisionista", presentation: "modal"}}/>
	
	        </Stack.Navigator>
	
	    );
	
	};
	
	  
	
	const Tab = createBottomTabNavigator();
	
	function TabGroup(){
	
	    return (
	
	        <Tab.Navigator
	
	        screenOptions={({ route }) => ({
	
	            tabBarIcon: ({ focused, color, size }) => {
	
	                let iconName;
	
	                if (route.name === 'Feed') {
	
	                    iconName = 'home';
	
	                } else if (route.name === 'Comisionistas') {
	
	                    iconName = 'barschart';
	
	                } else if (route.name === 'Productos') {
	
	                    iconName = 'shoppingcart';
	
	                }
	
	                return <AntDesign name={iconName} size={size} color={color} />;
	
	            },
	
	        })}
	
      >	
	
	            <Tab.Screen name="Feed" component={FeedStack} options={{headerShown: false}}/>
	
	            <Tab.Screen name="Productos" component={Tab2Stack} options={{headerShown: false}} />
	
	            <Tab.Screen name="Comisionistas" component={Tab3Stack} options={{headerShown: false}}/>
	
	        </Tab.Navigator>
	
	    )
	
	}
	
	  
	
	export default function Navigation() {
	
	    return (
	
	    <NavigationContainer>
	
	        <TabGroup/>
	
	    </NavigationContainer>
	
	    );
	
	    }
- mi ./app/redux/slices/Users.js
	  

	const initialState = {
	
	  currentUser: null,
	
	};
	
	  
	
	const userReducer = (state = initialState, action) => {
	
	  switch (action.type) {
	
	    case 'SET_USER':
	
	      return {
	
	        ...state,
	
	        currentUser: action.payload,
	
	      };
	
	    default:
	
	      return state;
	
	  }
	
	};
	
	  
	
	export default userReducer;