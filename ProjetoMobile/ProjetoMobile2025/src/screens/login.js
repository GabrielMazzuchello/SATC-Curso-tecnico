import {StyleSheet, Text, View, Image, TextInput, ImageBackground} from "react-native"
import imagemFundo from "../assets/netflix.png"

export function Login () {
    return(

    <View style={styles.login}>
            <ImageBackground style={{flex: 1, widht: '100%', height: '100%'}} source={imagemFundo}>
            </ImageBackground>
        <View>
            <TextInput style={styles.input} placeholder='Digite seu nome aqui: '/>
            <TextInput style={styles.input} placeholder='Digite sua idade aqui: '/>
        </View>
    </View>
    
);
}

const styles = StyleSheet.create({
container: {
    flex: 1, 
    alignItems: "center", 
    justifyContent: "center", 
    backgroundColor: "#20CFFF"
},
login: {
    flex:1,
    backgroundColor: '#000',
    fontSize: 20,
},
img1 : {
    width: 200,
    height: 200,
},
img2 : {
    width: 200,
    height: 200,
},
text1: {
    flex: 1
},
text2 : {
    flex: 2,
    alignSelf: 'flex-end',
    marginRight: 20 
},
text3 : {
    flex: 3,
    alignSelf: 'center' 
},
imgs: {
    justifyContent: 'space-evenly',
    flexDirection: 'row'
},
texts: {
    margin: 'auto', 
    color: 'red',
    fontSize: 30,
    fontWeight: 'bold',
},
input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
}  
})