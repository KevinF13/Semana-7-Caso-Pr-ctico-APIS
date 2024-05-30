import { Document } from 'mongoose';

export interface Inventario extends Document {
  readonly nombre: string;
  readonly descripcion?: string;
  readonly cantidad: number;
  readonly precio: number;
}
