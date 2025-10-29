import axios from "axios";
import React, { useState } from "react";

interface Metrica {
  nome: string;
  request: string;
}
interface MetricasData {
  acuracia: number;
  precisao: number;
  recall: number;
  fscore: number;
  reviews: [{review: string, saida: boolean, esperado: boolean}];
}
export default function Metricas({nome, request}: Metrica) {

  const buscar = async (e: React.MouseEvent<HTMLButtonElement, MouseEvent>, filtro: number) => {
    e.preventDefault();
    axios.get(`http://localhost:5000/${request}`, { params: { "filtro":filtro , "fold": fold } })
      .then(response => {
        if (filtro === 0) {
          setMetricasSemFiltro(response.data);
        } else {
          setMetricas(response.data);
        }
      })
      .catch(error => {
        console.error("Erro ao buscar métricas:", error);
      });
  }

  const [metricas, setMetricas] = useState<MetricasData>();
  const [metricasSemFiltro, setMetricasSemFiltro] = useState<MetricasData>();
  const [state, setState] = useState<boolean>(true);
  const [fold, setFold] = useState<number>(0);

  const foldar = (value: string) => {
    const newValue = parseInt(value);
    if (!isNaN(newValue) && newValue >= 0 && newValue <= 3) {
      setFold(newValue);
    }
  }

  const trocar = () => {
    setState(!state);
  }

  return (    
    <div className="bg-white my-5 rounded-lg shadow-lg relative flex flex-col items-center">
      <div className="grid grid-cols-3 gap-5 m-2 py-3 border-b">
        <h1 className="text-2xl font-bold ">{nome}</h1>

        <button className="bg-amber-500 rounded-2xl px-2 py-0 inline
         hover:bg-amber-700 text-white"
         onClick={()=> trocar()}>
          Trocar - {state ? "Com Filtro" : "Sem Filtro"}
        </button>
        <div className="border-l-2 pl-2">
          <h2>Fold combinação</h2>
          <input className="font-bold border rounded-lg pl-2" type="number" defaultValue={0} min={0} max={3} onChange={(e)=>foldar(e.target.value)}/>
        </div>
      </div>
       
      {state && <ul>
          {
            metricas && (
              <>
                <li className="border-b p-2"><strong>Acurácia:</strong> {metricas.acuracia}</li>
                <li className="border-b p-2"><strong>Precisão:</strong> {metricas.precisao}</li>
                <li className="border-b p-2"><strong>Recall:</strong> {metricas.recall}</li>
                <li className="border-b p-2"><strong>F1-Score:</strong> {metricas.fscore}</li>
              </>
            )}
          {metricas && (metricas.reviews.map((item, index) => (
            <li key={index} className="border-b p-2">
              <p><strong>Review:</strong> {item.review}</p>
              <p><strong>Saída:</strong> {item.saida ? "Positivo" : "Negativo"}</p>
              <p><strong>Esperado:</strong> {item.esperado ? "Positivo" : "Negativo"}</p>
            </li>
          )))}
      </ul>}
      {!state && <ul>
          {
            metricasSemFiltro && (
              <>
                <li className="border-b p-2"><strong>Acurácia:</strong> {metricasSemFiltro.acuracia}</li>
                <li className="border-b p-2"><strong>Precisão:</strong> {metricasSemFiltro.precisao}</li>
                <li className="border-b p-2"><strong>Recall:</strong> {metricasSemFiltro.recall}</li>
                <li className="border-b p-2"><strong>F1-Score:</strong> {metricasSemFiltro.fscore}</li>
              </>
            )}
          {metricasSemFiltro && (metricasSemFiltro.reviews.map((item, index) => (
            <li key={index} className="border-b p-2">
              <p><strong>Review:</strong> {item.review}</p>
              <p><strong>Saída:</strong> {item.saida ? "Positivo" : "Negativo"}</p>
              <p><strong>Esperado:</strong> {item.esperado ? "Positivo" : "Negativo"}</p>
            </li>
          )))}
      </ul>}

      <div className="m-2 flex gap-3">
        <button className="bg-sky-500 rounded-2xl p-1
        hover:bg-sky-700 text-white"
        onClick={(e)=>buscar(e, 1)}>
          INICIAR COM FILTRO
        </button>
        <button className="bg-emerald-500 rounded-2xl p-1
          hover:bg-emerald-700 text-white"
          onClick={(e)=>buscar(e, 0)}>
          INICIAR SEM FILTRO
        </button>
      </div>
      
    </div>
  )
}