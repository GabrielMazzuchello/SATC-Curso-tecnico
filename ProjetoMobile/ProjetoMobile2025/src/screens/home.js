import {StyleSheet, Text, View, Image, ImageBackground} from "react-native"
import imagemFundo from "../assets/netflix.png"

export function Home () {
    return(
        <View style={styles.home}>
            <ImageBackground style={{flex: 1, widht: '100%', heigh: '100%'}} source={imagemFundo}>
            </ImageBackground>
        <View style={styles.text1}>
            <Text style={styles.texts}>Zécaflix</Text> 
        </View>
        <View style={styles.imgs}>
            <Image style={styles.img1} source={{uri:'https://m.media-amazon.com/images/I/91RzpxQktRL.jpg'}}/>
            <Image style={styles.img1} source={{uri:'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKr78LlQAp91G2kspqG75p-EFtZ8r11hxEVg&s'}}/>
        </View>
        <View style={styles.text2}>
            <Text style={styles.texts}>Assista já!</Text>
        </View>
        <View style={styles.imgs}>
            <Image style={styles.img2} source={{uri:'https://m.media-amazon.com/images/M/MV5BMjU0NWMzOWMtZjM0MC00ZTE0LThmYzItZGQ1N2JmNDU1NGI4XkEyXkFqcGc@._V1_.jpg'}}/>
            <Image style={styles.img2} source={{uri:'https://i.ebayimg.com/images/g/3TYAAOSwO0lkwEQu/s-l400.jpg'}}/>
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
home: {
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
}  
})