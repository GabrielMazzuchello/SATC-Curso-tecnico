import { registerWebModule } from "expo";
import {StyleSheet, Text, View} from "react-native"

export default function Gallery () {
    return(
        <View style={styles.container}>
            <Text>Esta é a galeria!</Text> 
        </View>
    );
}

export function Favorites () {
    return(
        <View style={styles.container}>
            <Text>Este é o favoritos!</Text> 
        </View>
    );
}

export function Profile () {
    return(
        <View style={styles.container}>
            <Text>Este é o perfil!</Text> 
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#20CFFF"
    }
})