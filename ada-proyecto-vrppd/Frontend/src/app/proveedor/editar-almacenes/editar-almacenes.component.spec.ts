import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditarAlmacenesComponent } from './editar-almacenes.component';

describe('EditarAlmacenesComponent', () => {
  let component: EditarAlmacenesComponent;
  let fixture: ComponentFixture<EditarAlmacenesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EditarAlmacenesComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditarAlmacenesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
