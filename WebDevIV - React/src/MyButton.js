function updater(counter, setCounter){
    setCounter(counter++);
}

function MyButton({name, counter, setCounter}) {
    return(
        <button onClick={
            updater(counter,setCounter)
        }>{name}</button>
    )
}


export default MyButton;