import './App.css'
import Metricas from './Components/Metricas'

function App() {
  
  return (
    <div className="bg-sky-300 min-h-screen grid grid-cols-4 gap-5">
      <Metricas nome={"Modelo MLP"} request={"mlp"}/>
      <Metricas nome={"Modelo SVM"} request={"svm"}/>
      <Metricas nome={"Modelo SGD"} request={"sgd"}/>
      <Metricas nome={"Modelo NAIVE BAYES"} request={"naive"}/>
    </div>
  )
}

export default App
